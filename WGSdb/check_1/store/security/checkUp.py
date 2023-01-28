a = 1;b = 2;c = 3;d = 4;e = 5;f = 6;
g = 7;h = 8;i = 9;j = 0;letters = [
'a','b','c','d','e','f','g','h',
#0   1   2   3   4   5   6   7
'i','j','k','l','m','n','o','p',
#8   9  10  11  12  13   14  15
'q','r','s','t','u','v','w','x',
#16  17  18 19  20  21  22  23
'y','z'
#24  25
];encNum = ('%d%d%d%d%d%d%d%d' % 
(b,g,h,e,i,i,a,j
 ));encLet1 = (
letters[1] + letters[0] + letters[17] +
letters[19] + letters[22] + letters[4] +
letters[11]
);encNumLet = ('%s%s' % 
(encNum,encLet1
 ));host_name = ('get_%s_as_host' % 
(encLet1));#print(host_name)