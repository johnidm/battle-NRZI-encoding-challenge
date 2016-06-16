def nrzi(transmisson: str) -> str:

    def check_health() -> None:
        
        if not transmisson:
            raise Exception('Transmission is empty')

        if transmisson[0] not in ['_', '¯']:
            # Validate high and low signal
            raise Exception(
                'The token {} is not a high or low signal'.format(transmisson[0]))

        for token in transmisson:
            if token not in ['_', '¯', '|']:
                Exception(
                    'Token {} is invalid int transmission segment'.format(token))

    check_health()

    give_bit = lambda bit: str((0, 1)[bit])

    bits = '0'  # start with bit 0
    change_signal = False

    # Skip first element, bacause first bit always is 0
    for token in transmisson[1:]:

        # When changed signal current bit should be 1
        # In other cases alway bit is 0
        current_bit = give_bit(change_signal)

        # When signal | is detected the next bit always be 1
        if token == '|':
            change_signal = True
            continue
        else:
            change_signal = False

        bits += current_bit

    return bits
