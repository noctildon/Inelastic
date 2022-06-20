"""
This script make bigstick outputs be compatible with 7o mathematica code
Input: ar40.dres
Output: ar40_obdmXX.dat, where XX refers to initial and final state

"""

# valence orbits: n, 2j, l, N
sdpf = [[0, 5, 2, 2], [1, 1, 0, 2], [0, 3, 2, 2],
        [0, 7, 3, 3], [1, 3, 1, 3], [0, 5, 3, 3], [1, 1, 1, 3]]


orbits = sdpf

headline = 'ONE-BODY DENSITY MATRIX FOR 2JO = {} TO =, {}\n'
threshold = 1e-5
def dres2dat(input, output):
    out = ''
    with open(input) as f:
        lines = f.readlines()
        Jt = float(lines[2].split()[2][0])

        out += headline.format(int(Jt*2), 0)
        for n in range(3, len(lines)):
            orba, orbb, me0, me1 = lines[n].split()
            e = [orba, orbb, me0, me1]
            if abs(float(me0)) > threshold:
                out += genDenLine(e,0)

        out += headline.format(int(Jt*2), 2)
        for n in range(3, len(lines)):
            orba, orbb, me0, me1 = lines[n].split()
            e = [orba, orbb, me0, me1]
            if abs(float(me1)) > threshold:
                out += genDenLine(e,1)

    print(out)
    save(out, output)


def save(content, filename):
    with open(filename, 'w') as f:
        f.write(content)


def genDenLine(e, T0):
    n_index = 3 # N principal quantum number
    # n_index = 0 # n nodal/radial quantum number
    orbit_in = orbits[int(e[0]) - 1]
    orbit_out = orbits[int(e[1]) - 1]
    N_in = orbit_in[n_index]
    j_in = orbit_in[1]
    N_out = orbit_out[n_index]
    j_out = orbit_out[1]

    if T0 == 0:
        return '{} {} {} {}   {}\n'.format(N_in, j_in, N_out, j_out, e[2])
    elif T0 == 1:
        return '{} {} {} {}   {}\n'.format(N_in, j_in, N_out, j_out, e[3])


# extract n=i->j from .dres files
# ground state is n=1
def preprocess(input, output, statej=2, statei=1):
    matrix = ''
    starting_line, ending_line = 0, 0
    with open(input) as f:
        unsplit_lines = f.readlines()
        lines = []
        for line in unsplit_lines:
            line = line.split()
            if line and '++++' in line[0]:
                line = []
            lines.append(line)

        for i in range(len(lines)):
            if 'Initial' in lines[i] and 'state' in lines[i]:
                if statei == int(lines[i][3]) and statej == int(lines[i+1][3]):
                    starting_line = i

        while True:
            line_pivot = starting_line + ending_line
            if lines[line_pivot] == []:
                break
            ending_line += 1
        ending_line = starting_line + ending_line

        for l in range(starting_line, ending_line):
            matrix += unsplit_lines[l]
    # print(matrix)
    save(matrix, output)


# Input ar40.dres (bigstick output) as file1
# Output ar40_obdmXX.dat, the input for the mathematica file (XX are some numbers), as file3
# One needs to specify the transition by statei and statej
def main(statej):
    statei = 1

    nucleus = 'ar40'
    file1 = nucleus + '.dres'
    file2 = 'DMfiles/' + nucleus + '_obdm' + str(statej) + '.dres'
    file3 = 'DMfiles/' + nucleus + '_obdm' + str(statej) + '.dat'

    preprocess(file1, file2 ,statej=statej, statei=statei)
    dres2dat(file2, file3)


if __name__ == "__main__":
    # this generates ar40_obdm11.dat (or just ar40_obdm1.dat),
    # which contains the density matrices for the transition from n=1->1
    main(1)