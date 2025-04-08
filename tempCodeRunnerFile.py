
pivot = df.pivot(index="player A", columns="player B", values="A's point")
plt.figure(figsize=(10, 8))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title("A's Total Points vs B's Strategy")
plt.tight_layout()
plt.show()