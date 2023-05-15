#!/usr/bin/env python
import tika
tika.initVM()
from tika import parser, language
parsed = parser.from_file('robotics-11-00130-v2.pdf')
print(parsed["metadata"])
# print(parsed["content"])