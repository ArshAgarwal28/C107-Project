import pandas as pd
import plotly.express as px

marks_data = pd.read_csv("data.csv")

student_mean_level = marks_data.groupby(["student_id", "level"],
                                        as_index=False)["attempt"].mean()
print(student_mean_level)

fig = px.scatter(student_mean_level, x="student_id", y="level",
                 size="attempt", color="attempt")

fig.show()
