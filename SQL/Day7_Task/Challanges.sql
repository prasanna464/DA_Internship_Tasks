Problem Statement Link :- https://www.hackerrank.com/challenges/challenges/problem

SELECT
    h.hacker_id,
    h.name,
    COUNT(c.challenge_id) AS total
FROM Hackers h
JOIN Challenges c
    ON h.hacker_id = c.hacker_id
GROUP BY
    h.hacker_id,
    h.name
HAVING
    total = (
        SELECT MAX(challenge_count)
        FROM (
            SELECT COUNT(challenge_id) AS challenge_count
            FROM Challenges
            GROUP BY hacker_id
        ) AS counts
    )
    OR total IN (
        SELECT challenge_count
        FROM (
            SELECT COUNT(challenge_id) AS challenge_count
            FROM Challenges
            GROUP BY hacker_id
        ) AS counts
        GROUP BY challenge_count
        HAVING COUNT(challenge_count) = 1
    )
ORDER BY
    total DESC,
    h.hacker_id;
