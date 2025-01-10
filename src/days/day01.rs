use crate::{Solution, SolutionPair};
use itertools::*;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let input = std::fs::read_to_string("input/day1.txt").unwrap();
    let (mut left_col, mut right_col) = parse(&input);

    left_col.sort();
    right_col.sort();
    let counts = right_col.iter().counts();

    let sol1: i32 = left_col
        .iter()
        .zip(right_col.iter())
        .map(|(i_left, i_right)| (i_left - i_right).abs())
        .sum();

    let sol2: i32 = left_col
        .iter()
        .map(|i| i * counts.get(&i).copied().unwrap_or(0) as i32)
        .sum();

    return (Solution::from(sol1), Solution::from(sol2));
}

fn parse(input: &str) -> (Vec<i32>, Vec<i32>) {
    let (mut ls1, mut ls2) = (vec![], vec![]);
    for line in input.lines() {
        let (i1, i2) = line.split_whitespace().collect_tuple().unwrap();
        ls1.push(i1.parse().unwrap());
        ls2.push(i2.parse().unwrap());
    }
    return (ls1, ls2);
}
