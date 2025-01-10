use crate::{Solution, SolutionPair};
use itertools::*;
use std::fs::read_to_string;

///////////////////////////////////////////////////////////////////////////////

pub fn solve() -> SolutionPair {
    let master_list = read_to_string("input/day2.txt").unwrap();

    let reports: Vec<Vec<i32>> = master_list
        .lines()
        .map(|report| {
            report
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect()
        })
        .collect();

    let sol1 = reports.iter().filter(|r| filter_1(r)).count();

    let sol2 = reports.iter().filter(|r| filter_2(r)).count();

    (Solution::from(sol1), Solution::from(sol2))
}

fn filter_1(report: &[i32]) -> bool {
    let sign = (report[0] - report[1]).signum();
    return report
        .iter()
        .tuple_windows()
        .all(|(a, b)| (a - b) * sign > 0 && (a - b).abs() <= 3);
}

fn filter_2(report: &[i32]) -> bool {
    (0..report.len())
        .map(|ix| remove_element(report, ix))
        .any(|r| filter_1(&r))
}

fn remove_element(report: &[i32], idx: usize) -> Vec<i32> {
    let mut cloned = report.to_owned();
    cloned.remove(idx);
    return cloned;
}
