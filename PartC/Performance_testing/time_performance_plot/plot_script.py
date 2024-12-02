import matplotlib.pyplot as plt

# Data from experiment runs
data = {
    "Number of TODOs": [1, 10, 100, 1000],
    "Add Times Run 1": [0.02454233169555664, 0.0020041465759277344, 0.002508401870727539, 0.001508474349975586],
    "Update Times Run 1": [0.00551605224609375, 0.001999378204345703, 0.0015041828155517578, 0.002003908157348633],
    "Delete Times Run 1": [0.003002643585205078, 0.0020008087158203125, 0.001005411148071289, 0.00099945068359375],
    "Add Times Run 2": [0.0045092105865478516, 0.0010035037994384766, 0.0010080337524414062, 0.0010082721710205078],
    "Update Times Run 2": [0.0009989738464355469, 0.0015032291412353516, 0.0015065670013427734, 0.0009984970092773438],
    "Delete Times Run 2": [0.0020046234130859375, 0.0010056495666503906, 0.0010042190551757812, 0.0009968280792236328],
}

# Compute averages
average_add = [
    (data["Add Times Run 1"][i] + data["Add Times Run 2"][i]) / 2 for i in range(len(data["Number of TODOs"]))
]
average_update = [
    (data["Update Times Run 1"][i] + data["Update Times Run 2"][i]) / 2 for i in range(len(data["Number of TODOs"]))
]
average_delete = [
    (data["Delete Times Run 1"][i] + data["Delete Times Run 2"][i]) / 2 for i in range(len(data["Number of TODOs"]))
]

# Generate the plot
plt.figure(figsize=(10, 6))

plt.plot(data["Number of TODOs"], average_add, marker='o', label="Add (Average)")
plt.plot(data["Number of TODOs"], average_update, marker='s', label="Update (Average)")
plt.plot(data["Number of TODOs"], average_delete, marker='^', label="Delete (Average)")

# Customize the plot
plt.title("Average Time taken of TODO API Operations")
plt.xlabel("Number of TODOs")
plt.ylabel("Time Taken (seconds)")
plt.xscale("log")
plt.xticks(data["Number of TODOs"], labels=data["Number of TODOs"])
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()

# Show the plot
plt.show()
