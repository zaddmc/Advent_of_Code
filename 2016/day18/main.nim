import std/strutils
proc is_trap(sample:string):bool =
  return sample in ["^^.", ".^^", "^..", "..^"]

proc evolve(start:string):string =
  var work = " ".repeat(len(start))
  for idx, chr in start:
    let left = if idx > 0: start[idx - 1] else: '.'
    let right = if idx < len(start) - 1: start[idx + 1] else: '.'
    let sample = left & start[idx] & right
    work[idx] = if is_trap(sample): '^' else: '.'
  return work

proc main(seed:string, steps:int):int =
  var thing = seed
  var safe_tiles = 0
  for i in 0..steps:
    safe_tiles += thing.count(".")
    thing = evolve(thing)
  return safe_tiles

when isMainModule:
  let input = read_file("input.txt").strip()
  let part1 = main(input, 39)
  let part2 = main(input, 399999)

  echo(part1)
  echo(part2)
