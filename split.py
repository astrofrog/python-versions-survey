# Open file
f = open('versions.csv', 'r')

# Read header line
header = f.readline()

f_astro = open('versions-astro.csv', 'w')
f_other = open('versions-other.csv', 'w')

# Loop through lines and extract astronomers from other users
for line in f:
    try:
        field = line.strip().split(',')[-1].lower()
    except ValueError:
        field = 'unknown'
    if 'planetary' in field \
        or 'galaxy' in field \
        or 'astro' in field \
        or 'cosmo' in field \
        or 'asrtronomy' in field \
            or 'solar' in field:
        f_astro.write(line)
    else:
        f_other.write(line)
