# Using regular expressions


# Importing the package

import re


# Reference code

pattern = "+233"


# Matching the Code with text

"Match" if re.fullmatch(pattern, "+234") else "No match"


