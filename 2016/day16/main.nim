import std/strutils

proc inverse(str:string):string =
  var output: string
  for i in countdown(str.high, 0):
    output &= (if str[i] == '1': "0" else: "1" )
  return output

proc checksum(str:string):string =
  var a = str
  var b = ""
  while len(a) mod 2 == 0:
    for idx in countup(0, len(a)-1, 2):
      b &= (if a[idx] == a[idx+1]: "1" else: "0")
    a = b
    b = ""
  return a
 
proc main(start:string, size:int):string=
  var a = start
  var b:string

  while len(a) < size:
    b = inverse(a)
    a &= "0" & b

  let chks = checksum(a[0..size-1])
  return chks

proc get_data():string =
  let data = read_file("input.txt").strip()
  return data

when isMainModule:
  let data = get_data()
  let part1 = main(data, 272)
  let part2 = main(data, 35651584)

  echo("Part1: ", part1)
  echo("Part2: ", part2)
  # echo(main("10000", 20))

