distanceMatrix = [[0, 12, 12, 13, 15, 15],
                  [12, 0, 2, 6, 8, 8],
                  [12, 2, 0, 6, 9, 9],
                  [13, 6, 6, 0, 8, 8],
                  [15, 8, 9, 8, 0, 4],
                  [15, 8, 9, 8, 4, 0]]


speciesList = ["M_Spacii", "T_Pain", "G_Unit", "Q_Doba", "R_Mani", "A_Finch"]


def UPGMA(dM, sp):
    while (len(dM) > 1):
        # finds the smallest non-0 matrix coordinate
        leastRow, LeastCol = findSmallest(dM)
        dist = dM[leastRow][LeastCol]
        # Create a new branch in the output tree
        # This is the function you are writing. See bottom of cell
        dM = updateMatrix(dM, leastRow, LeastCol)
        # updates the species list
        sp = updateSpecies(sp, leastRow, LeastCol, dist)
    return ''.join(sp)


def findSmallest(dM):  # finds the smallest non-0 matrix coordinate
    # Search the matrix for the coordinate of the shortest distance between organisms
    min_value = float('inf')
    min_coords = (-1, -1)

    # Loop through each row and column of the matrix
    for i in range(len(dM)):
        for j in range(len(dM[i])):
            # Skip diagonal elements and check for a new minimum
            if i != j and dM[i][j] < min_value:
                min_value = dM[i][j]
                min_coords = (i, j)

    row, col = min_coords
    return row, col


def updateSpecies(sp, r, c, dist):  # updates the species list
    merged_species = f"({sp[r]},{sp[c]}:{dist})"
    sp[r] = merged_species
    del sp[c]
    return sp


def updateMatrix(dM, row, col):
    newMat = []
    # Calculate the new distances to the merged cluster
    # and build the new distance matrix
    for i in range(len(dM)):
        # Skip the rows for the clusters that were merged
        if i != row and i != col:
            new_row = []
            for j in range(len(dM[i])):
                # Skip the columns for the clusters that were merged
                if j != row and j != col:
                    new_row.append(dM[i][j])
            # Compute the distance to the new cluster
            dist_to_new_cluster = (
                dM[i][row] + dM[i][col]) / 2
            # Insert at the beginning of the new row
            new_row.insert(row, dist_to_new_cluster)
            newMat.append(new_row)

    # Add the row for the new cluster
    new_cluster_row = [0]  # Distance from the new cluster to itself is 0
    for i in range(0, len(newMat)):  # Start from 1 to skip the distance to itself
        # The first element in each row is the distance to the new cluster
        new_cluster_row.append(newMat[i][row])

    # Shift the values at index 0 and 1
    value_at_index_0 = new_cluster_row.pop(0)
    new_cluster_row.insert(row, value_at_index_0)
    newMat.insert(row, new_cluster_row)
    return newMat


if __name__ == "__main__":
    print(UPGMA(distanceMatrix, speciesList))
