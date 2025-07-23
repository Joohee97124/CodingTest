def solution(letter):
    #answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    #for let in letter.split():
    #    answer += morse.get(let)
    
    #answer = ''.join([morse.get(let) for let in letter.split()])    
    return ''.join([morse.get(let) for let in letter.split()]) 