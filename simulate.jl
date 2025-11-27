using DelimitedFiles
using Plots

data = readdlm("initial_data.txt")
coordinates = data[:, 1:3]
speed = data[:, 4:end]
scatter3d(coordinates[:, 1], coordinates[:, 2], coordinates[:, 3],
          markersize = 2,
          markercolor = :red,
          xlabel = "X Label",
          ylabel = "Y Label",
          zlabel = "Z Label",
          legend = false)
