import select
import socket
import sys
import queue

'''

https://pymotw.com/3/select/

'''

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address),
      file=sys.stderr)
server.bind(server_address)
server.listen(5)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    print('waiting for the next event', file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print('  connection from', client_address,
                  file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)

            # Give the connection a queue for data
            # we want to send
            message_queues[connection] = queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print('  received {!r} from {}'.format(
                    data, s.getpeername()), file=sys.stderr,
                )
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
                else:
                    # Interpret empty result as closed connection
                    print('  closing', client_address,
                          file=sys.stderr)
                    # Stop listening for input on the connection
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()

                    # Remove message queue
                    del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No messages waiting so stop checking
            # for writability.
            print('  ', s.getpeername(), 'queue empty',
                  file=sys.stderr)
            outputs.remove(s)
        else:
            print('  sending {!r} to {}'.format(next_msg,
                                                s.getpeername()),
                  file=sys.stderr)
            s.send(next_msg)

    # Handle "exceptional conditions"
    for s in exceptional:
        print('exception condition on', s.getpeername(),
              file=sys.stderr)
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del message_queues[s]