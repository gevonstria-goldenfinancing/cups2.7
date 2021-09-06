import random
import string


class CupsGenerator:

    def generate(self):
        ree_id = self._generate_ree_id()
        dist_id = self._generate_dist_id()
        print ree_id
        print dist_id
        control = int(ree_id + dist_id) % 529
        division = control / 23
        mod = control % 23
        control_letter = self._get_control_numbers_by(int(division))
        control_2_letter = self._get_control_numbers_by(mod)

        return "ES " +ree_id +" " +dist_id +" " +control_letter +" " +control_2_letter

    def _generate_ree_id(self):
        id = random.randint(0, 9999)
        return str(id)

    def _generate_dist_id(self):
        id = random.randint(0, 999999999999)
        return str(id)

    def _get_control_numbers_by(self, number):
        return self._get_control_numbers()[number]

    def _get_control_numbers(self):
        return [
            'T',
            'R',
            'W',
            'A',
            'G',
            'M',
            'Y',
            'F',
            'P',
            'D',
            'X',
            'B',
            'N',
            'J',
            'Z',
            'S',
            'Q',
            'V',
            'H',
            'L',
            'C',
            'K',
            'E',
        ]

