import std/strutils
import std/bitops
import std/sugar

discard """
This stupid fucking challenge is just math
https://www.geeksforgeeks.org/dsa/josephus-problem/
Fuck math
"""

proc main_part1(n_elves:int):int =
  var elves: seq[int]
  for i in countup(1, n_elves):
    elves.add(i)
    
  var offset = 0
  while len(elves) > 1:
    let odd_length = len(elves) mod 2
    elves = collect: 
      for i in countup(offset, len(elves) - 1, 2): elves[i]
    
    offset = offset.bitxor(odd_length)
  return elves[0]

proc main_part1_v2(n:int):int =
  var i = 1
  var ans = 0

  while i <= n:
    ans = (ans + 2) mod i
    i += 1
  return ans + 1

proc main_part2(n:int):int =
  var i = 1
  while i * 3 < n:
    i *= 3

  if n <= 2*i:
    return n - i
  return 2*n - 3*i

when isMainModule:
  let input = read_file("input.txt").strip().parseInt()
  let part1 = main_part1(input)
  let part1_2 = main_part1_v2(input)
  assert part1 == part1_2

  let part2 = main_part2(input)

  echo(part1)
  echo(part2)
