def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMult(line, index):
    token = {'type': 'MULT'}
    return token, index + 1

def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMult(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    line2 = []  #array only plus & minus 
    while index < len(tokens):  #calculate mult & div
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index-1]['type'] == 'PLUS':
                line2.append('PLUS')
                line2.append(tokens[index]['number'])
            elif tokens[index-1]['type'] == 'MINUS':
                line2.append('MINUS')
                line2.append(tokens[index]['number'])
            elif tokens[index-1]['type'] == 'MULT':
                if tokens[index-3]['type'] == 'MULT' or 'DIV':
                    numb = line2[-1]   # the end of array
                    line2.pop()  # delete the end of array
                    line2.append(numb * tokens[index]['number']) # add new result
                else:
                    line2.pop()
                    line2.append(tokens[index-2]['number'] * tokens[index]['number'])
            elif tokens[index-1]['type'] == 'DIV':
                if tokens[index-3]['type'] == 'MULT' or 'DIV':
                    numb = line2[-1]
                    line2.pop()
                    line2.append(numb / tokens[index]['number'])
                else:
                    line2.pop()
                    line2.append(tokens[index-2]['number'] / tokens[index]['number'])
        index += 1
    return secondevaluate(line2)

    
def secondevaluate(line2):
    answer = 0
    index = 0
    while index < len(line2):  #calculate plus & minus
        if line2[index] == 'PLUS':
            answer += line2[index+1]
        elif line2[index] == 'MINUS':
            answer -= line2[index+1]
        else:
            print 'Invalid syntax'
        index += 2
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)

# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1*2", 2)
    test("4/2", 2)
    test("1+2", 3)
    test("3-1", 2)
    test("1*2+6-3", 5)
    test("8/4*2", 4)
    test("1.0/4.0+1.2*4", 5.05)
    test("3+4-5*1.8", -2)
    test("5.0/2.0-3*4+6/2+1", -5.5)
    test("5/2-3*4+6/2+1", -5.5)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
print "answer = %f\n" % answer
