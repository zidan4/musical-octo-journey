def mutate_payload(self,original_payload):
  # pick a simple mutator or even call an external script
  picker = random.randint(1,3)
  # select a random offset in the payload to mutate
  offset = random.randint(0,len(original_payload)-1)
  payload = original_payload[:offset]
  # random offset insert a SQL injection attempt
  if picker == 1:
    payload += "'"
    
  # jam an XSS attempt in
  if picker == 2:
    payload += "<script>alert('BHP!');</script>"
  # repeat a chunk of the original payload a random number
  
  if picker == 3:
    chunk_length = random.randint(len(payload[offset:]),len(payload)-1)
    repeater = random.randint(1,10)
    for i in range(repeater):
      payload += original_payload[offset:offset+chunk_length]
      # add the remaining bits of the payload
      payload += original_payload[offset:]
      
  return payload
