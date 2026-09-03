import std/strutils

type PairSeq = seq[tuple[period:int, offset:int]]

proc load_data():PairSeq =
  var data: PairSeq
  let raw = read_file("input.txt").strip()
  for idx, line in pairs(raw.splitLines):
    let period = parseInt(line[12..13].strip())
    let offset = parseInt($line[^2]) + idx
    data.add((period,offset))
  return data

proc brute(data:PairSeq):int =
  var loop:Natural = 0
  while true:
    var flag = false
    for pair in data:
      let pos = (loop + pair.offset) mod pair.period
      if pos == 0:
        flag = true
      else:
        flag = false
        break

    if flag:
      return loop - 1
    loop += 1

  

when isMainModule:
  var data = load_data()
  let part1 = brute(data)
  data.add((11,len(data)))
  let part2 = brute(data)
  echo(part1)
  echo(part2)
  
