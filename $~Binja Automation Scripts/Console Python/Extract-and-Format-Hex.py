#WARNING: See section in Workflow about identifying data types by viewing hex. You can extract all you like, but it won't work if it, for example, only actually reads every 4 bytes (with the rest being padding bytes)!
#Extract Hex bytes from data location for a given length. Takes everything, including padding!
$location = #<MEMORY LOCATION HERE, ex: 2000c3000 (extracted from "data_2000c3000")
$length = #<length of location to read in hex>
bytes = bv.read(0x$location, $length) #$location and $length are placeholders for the real values!) ex: bv.read(0x3600c3000, 0x14)
cleanBytes = print(','.join(f'0x{byte:02x}' for byte in bytes))

# With the above completed, Here's how to only read every 4th byte (including the starting byte):
every4th = cleanBytes.split(',')[::4]
cleanEvery4th = ','.join(every4th)
print(cleanEvery4th)
