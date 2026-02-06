use std::collections::HashSet;
use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("Should have read file");
    let stripped = contents.trim_end();
    let asdpk = stripped.split(", ");

    let mut path: HashSet<(i32, i32)> = HashSet::new();

    let mut dir = 0;
    let mut x = 0;
    let mut y = 0;

    for a in asdpk {
        if a.chars().nth(0) == Some('R') {
            dir += 1;
        } else {
            dir -= 1;
        }
        dir = (dir + 4) % 4;

        let dist_str = &a[1..];
        let dist = dist_str.parse::<i32>().unwrap();
        my_move(path, dist, dir);
        match dir {
            0 => x += dist,
            1 => y += dist,
            2 => x -= dist,
            3 => y -= dist,
            _ => println!("boring {dir}"),
        }
    }

    let x_o = x.abs();
    let y_o = y.abs();
    let output = x_o + y_o;
    println!("{output}");
}

fn my_move(path: HashSet<(i32, i32)>, distance: i32, dir: i32) {
    println!("{dir}");
}
