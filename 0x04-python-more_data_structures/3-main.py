#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript", "Ruby" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

set_1 = { "Python", "C", "Javascript", "DEM" }
set_2 = { "Bash", "C", "Ruby", "Perl", "DEM" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

set_1 = { "damskal", "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl", "Damskal" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
