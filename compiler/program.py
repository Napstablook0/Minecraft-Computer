"""Ce script permet la conversion du script assembleur en son langage machine, il ne doit pas être modifie a moins de savoir ce que vous faites"""



OP_CODE_MACHINE_LNG = {"ADD": "0000", "SUB": "0001", "OR": "0010", "BND": "0011", "LDI": "0100", "JMP": "0101", "JIF": "0110", "HLT": "1111    0000    0000    0000",
                       "JZ": "0101    0000", "JMP": "0110    0000", "AND": "0011"}
REGISTERS_MACHINE_LNG = {
    'r0': '0000', 'r1': '0001', 'r2': '0010', 'r3': '0011',
    'r4': '0100', 'r5': '0101', 'r6': '0110', 'r7': '0111',
    'r8': '1000', 'r9': '1001', 'r10': '1010', 'r11': '1011',
    'r12': '1100', 'r13': '1101', 'r14': '1110', 'r15': '1111'
}


class Assembly_program():

    def __init__(self, instructions: list[str]):
        assert type(instructions) == list, "instructions est une liste"
        for instr in instructions:
            assert type(instr) == str, "instructions contient que des str"



        self._instructions = instructions

        self._machine_code = self._convertMachineCode()

    
    def _convertMachineCode(self) -> list[str]:
        
        machine_code = []

        for instr in self._instructions:
            current_instr_code = []
            
            sep_instr = instr.split(" ")
            
            for mini_instr in sep_instr:

                if mini_instr in OP_CODE_MACHINE_LNG.keys():
                    current_instr_code.append(OP_CODE_MACHINE_LNG[mini_instr])

                elif mini_instr in REGISTERS_MACHINE_LNG:
                    current_instr_code.append(REGISTERS_MACHINE_LNG[mini_instr])
                
                elif mini_instr.isdigit():
                    mini_instr = "0" * (8-len(format(int(mini_instr), '04b'))) + format(int(mini_instr), '04b') # converti en binaire sur 8 bits
                    mini_instr = mini_instr[:4] + "    " + mini_instr[4:]
                    current_instr_code.append(mini_instr)

                else:
                    print("mauvaise instruction :", mini_instr)
                    return "CODE INVALIDE"
                
            machine_code.append(current_instr_code)
    

        return machine_code
    

    def getMachineCode(self):
        return self._machine_code