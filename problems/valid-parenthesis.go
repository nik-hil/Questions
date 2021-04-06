// Source: https://leetcode.com/problems/valid-parentheses/

func isValid(s string) bool {
    stacks := []rune{}
    maps := map[rune]rune{ '}': '{', ')':'(', ']':'['}
    
    for _, r := range s{
        if r == '{' || r == '[' || r == '('{
            stacks = append(stacks, r)
        }else{
            
            if len(stacks) == 0{
                return false
            }
            remove := maps[r]
            if stacks[len(stacks)-1] == remove{
                stacks = stacks[:len(stacks)-1]
            } else{
                break
            }
        }
    }
    return len(stacks) == 0
}
