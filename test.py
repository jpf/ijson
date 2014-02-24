import StringIO
from ijson.backends.python import basic_parse
from ijson.backends.python import parse
from ijson.backends.python import items

import pprint

json = '{ "a": { "b": 2, "c": 3 } }'
not_json = '''
{
    "org.gnu.Emacs" =     {
        ApplePressAndHoldEnabled = NO;
    };
    "org.gnu.Poop" =     {
        IsThisSilly = "Yes";
    };
    "org.gnu.Poops" =     {
        IsThisSilly = "No";
    };
}
'''
file_like = StringIO.StringIO(not_json)

file_like = open('../defaults-ns')

# for i in parse(file_like):
#     print i

i = next(items(file_like, ''))
pprint.pprint(i['com.apple.Terminal'])
