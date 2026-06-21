use crate::{Solution, SolutionPair};

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let values: Vec<i32> = std::fs::read_to_string("../day01/input.txt")
        .expect("Missing input")
        .lines()
        .map(|line| line.parse::<i32>().unwrap_or_default())
        .collect();

    let mut sol1: i32 = 0;
    let mut sol2: i32 = 0;

    for i in 0..values.len() {
        for j in i..values.len() {
            if sol1 == 0 && values[i] + values[j] == 2020 {
                sol1 = values[i] * values[j];
            }
            for k in i + 1..values.len() {
                if sol2 == 0 && values[i] + values[j] + values[k] == 2020 {
                    sol2 = values[i] * values[j] * values[k];
                }
            }
        }
    }
    return (Solution::from(sol1), Solution::from(sol2));
}
