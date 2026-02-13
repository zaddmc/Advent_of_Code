namespace MyApp;

internal class Program
{
    static Dictionary<string,Tuple<int,int?>> bots = new();
    static List<string> instructions = new();

    static void Main(string[] args)
    {
        StreamReader sr = new("input.txt");
        
        while (!sr.EndOfStream)
        {
            string line = sr.ReadLine()!;
            if (line.StartsWith("bot")) {
                instructions.Add(line);
                continue;
            }

            string[] parts = line.Split(" ", 6);

            string botIdx = parts[4] + parts[5];
            int.TryParse(parts[1], out int tokenVal);

            if (bots.ContainsKey(botIdx)){
                int orig_val = bots[botIdx].Item1;
                if (orig_val < tokenVal) {
                    bots[botIdx] = new(orig_val, tokenVal);
                } else {
                    bots[botIdx] = new(tokenVal, orig_val);
                }
            } else {
                bots[botIdx] = new(tokenVal, null);
            }
        }
        sr.Close();

        while (instructions.Count > 0)
        {
            string[] inst = new string[instructions.Count];
            instructions.CopyTo(inst);

            foreach (string line in inst)
            {
                string[] parts = line.Split(" ", 20);

                string botIdx = parts[0]+parts[1];
                string lowBotIdx = parts[5]+parts[6];
                string highBotIdx = parts[10]+parts[11];

                
                if (!bots.ContainsKey(botIdx)) continue;
                Tuple<int,int?> mainBot = bots[botIdx];
                if (!mainBot.Item2.HasValue) continue;

                if (mainBot.Item1 == 17 && mainBot.Item2 == 61) {
                    Console.WriteLine(botIdx);
                }

                assign(lowBotIdx, mainBot.Item1);
                assign(highBotIdx, mainBot.Item2.Value);
                instructions.Remove(line);
            }
        }
        int result = bots["output0"].Item1 * bots["output1"].Item1 * bots["output2"].Item1;
        Console.WriteLine(result);

    }

    static void assign(string botIdx, int compVal) {
        if (bots.ContainsKey(botIdx)) {
            Tuple<int,int?> lowBot = bots[botIdx];
            if (lowBot.Item2.HasValue) Console.WriteLine("Undefined Behavoir");
            if (lowBot.Item1 < compVal){
                bots[botIdx] = new(lowBot.Item1, compVal);
            } else {
                bots[botIdx] = new(compVal, lowBot.Item1);
            }
        } else {
            bots[botIdx] = new(compVal, null);
        }
    }
}
