package 난이도별.level01.두_정수_사이의_합;

public class sjjyy
{
    public static long solution(int a, int b)
    {
        long answer = 0;

        if (a <= b)
        {
            for (int i = a; i <= b; i++)
                answer += i;
        }
        else {
            for (int i = b; i <= a; i++)
                answer += i;
        }

        return answer;
    }

    public static long solution2(int a, int b)
    {
        long ans = 0;
        int x = Math.min(a, b);
        int y = Math.max(a, b);

        for(int i = x ; i <= y ; i++)
            ans += i;

        return ans;
    }

    public static void main(String [] args)
    {
        System.out.println(solution(3, 5)); // 12
        System.out.println(solution(3, 3)); // 3
        System.out.println(solution(5, 3)); // 12

        System.out.println(solution2(3, 5)); // 12
        System.out.println(solution2(3, 3)); // 3
        System.out.println(solution2(5, 3)); // 12
    }
}
