from scipy import stats

group_a = [85, 90, 78, 92, 88, 76, 95]
group_b = [70, 75, 80, 72, 68, 77, 74]

# Independent t-test
t_stat, p_value = stats.ttest_ind(
    group_a,
    group_b
)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Significant difference")
else:
    print("No significant difference")