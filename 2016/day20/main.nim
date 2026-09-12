import std/strutils
import std/algorithm

type Ranges = seq[tuple[lower:int,upper:int]]

proc parse_data(raw:seq[string]): Ranges =
  var parsed: Ranges
  for line in raw:
    let parts = line.split('-')
    let lower = parts[0].parseInt()
    let upper = parts[1].parseInt()
    parsed.add((lower,upper))
  return sorted(parsed)
  
proc main(ranges:Ranges):tuple[lowest:int, number:int] =
  var allowed = 0
  var lowest = 0
  var max_upper = 0
  for idx, line in ranges[0..^1]:
    let diff = max(0, line.lower - max_upper )
    # Check for first allowed value
    if lowest == 0 and diff != 0:
      lowest = max_upper
    allowed += diff
    max_upper = max(max_upper, line.upper + 1)
  return (lowest, allowed)

when isMainModule:
  let raw = read_file("input.txt").strip().splitLines()
  let ranges = parse_data(raw)

  let parts = main(ranges)
  echo parts.lowest
  echo parts.number
