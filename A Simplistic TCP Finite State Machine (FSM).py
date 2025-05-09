"""
Autômatos, ou Máquinas de Estados Finitos (MEF),
são extremamente úteis para programadores quando se trata de design de software.
Você receberá uma versão simplificada de uma MEF para codificar uma sessão TCP básica.

O resultado deste exercício será retornar o estado correto do TCP FSM com base na matriz de eventos fornecida.

A matriz de entrada de eventos consistirá em uma ou mais das seguintes strings:

APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK
Os estados são os seguintes e devem ser retornados em letras maiúsculas, conforme mostrado:

CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT
A entrada será um array de eventos. O estado inicial é CLOSED.
Sua tarefa é percorrer a FSM conforme determinado pelos eventos e retornar o estado final apropriado como uma string,
tudo em letras maiúsculas, conforme mostrado acima.

Se um evento não for aplicável ao estado atual, seu código retornará "ERROR".

Ação de cada evento sobre cada estado:
(o formato é INITIAL_STATE: EVENT -> NEW_STATE)

CLOSED: APP_PASSIVE_OPEN -> LISTEN
CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
LISTEN: RCV_SYN          -> SYN_RCVD
LISTEN: APP_SEND         -> SYN_SENT
LISTEN: APP_CLOSE        -> CLOSED
SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
SYN_RCVD: RCV_ACK        -> ESTABLISHED
SYN_SENT: RCV_SYN        -> SYN_RCVD
SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
SYN_SENT: APP_CLOSE      -> CLOSED
ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
FIN_WAIT_1: RCV_FIN      -> CLOSING
FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
CLOSING: RCV_ACK         -> TIME_WAIT
FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
TIME_WAIT: APP_TIMEOUT   -> CLOSED
CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
LAST_ACK: RCV_ACK        -> CLOSED
"""

def traverse_tcp_states(events):
    transitions = {
        ("CLOSED", "APP_PASSIVE_OPEN"): "LISTEN",
        ("CLOSED", "APP_ACTIVE_OPEN"): "SYN_SENT",
        ("LISTEN", "RCV_SYN"): "SYN_RCVD",
        ("LISTEN", "APP_SEND"): "SYN_SENT",
        ("LISTEN", "APP_CLOSE"): "CLOSED",
        ("SYN_RCVD", "APP_CLOSE"): "FIN_WAIT_1",
        ("SYN_RCVD", "RCV_ACK"): "ESTABLISHED",
        ("SYN_SENT", "RCV_SYN"): "SYN_RCVD",
        ("SYN_SENT", "RCV_SYN_ACK"): "ESTABLISHED",
        ("SYN_SENT", "APP_CLOSE"): "CLOSED",
        ("ESTABLISHED", "APP_CLOSE"): "FIN_WAIT_1",
        ("ESTABLISHED", "RCV_FIN"): "CLOSE_WAIT",
        ("FIN_WAIT_1", "RCV_FIN"): "CLOSING",
        ("FIN_WAIT_1", "RCV_FIN_ACK"): "TIME_WAIT",
        ("FIN_WAIT_1", "RCV_ACK"): "FIN_WAIT_2",
        ("CLOSING", "RCV_ACK"): "TIME_WAIT",
        ("FIN_WAIT_2", "RCV_FIN"): "TIME_WAIT",
        ("TIME_WAIT", "APP_TIMEOUT"): "CLOSED",
        ("CLOSE_WAIT", "APP_CLOSE"): "LAST_ACK",
        ("LAST_ACK", "RCV_ACK"): "CLOSED",
    }

    state = "CLOSED"

    for event in events:
        key = (state, event)
        if key not in transitions:
            return "ERROR"
        state = transitions[key]

    return state

print(traverse_tcp_states(["APP_ACTIVE_OPEN","RCV_SYN_ACK","RCV_FIN"]))