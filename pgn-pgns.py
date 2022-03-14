import os
import re
import pdb

pgn_type = "chess.com"

def find_all_occurence_indices(string, pattern):
    indices = [_.start() for _ in re.finditer(pattern, string)]
    # pdb.set_trace()
    return indices

def split_into_games(src_file,split_pattern):
    with open(src_file) as f:
        s = f.read()
    start_indices = find_all_occurence_indices(s,split_pattern)
    games = [s[start_indices[i]:start_indices[i+1]] for i in range(len(start_indices)-1 )]
    return games

if __name__ == "__main__":
    if pgn_type == "chess.com":
        split_pattern = '\[Event "Live Chess"\]'
    src_file_path = ""

    games = split_into_games(src_file_path,split_pattern)
    pdb.set_trace()


    
