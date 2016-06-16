
class NRZI():

    signal_change = '|'

    def econding(self, transmisson: str) -> str:

        give_bit = lambda bit: str((0, 1)[bit])

        current_bit = '0' # always start with bit 0 independente se a transmissao for alto-baixo baixo-alto
        
        bits = current_bit
        change_signal = False

        # Start always seccond elements, 
        # bacouse alwas first element is bit 0
        for token in transmisson[1:]:
            
            # When change_signal is flagged return 1
            current_bit = give_bit(change_signal)

            if token == NRZI.signal_change:
                change_signal = True
                continue
            else:
                change_signal = False

            bits += current_bit

        return bits