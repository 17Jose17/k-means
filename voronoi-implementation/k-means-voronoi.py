def kMeansVoronoi(points, k):

    class point:
        def __init__(self, xValues):
            self.coords = np.array(xValues)
    
        def get_coords(self):
            return self.coords.flatten()
        
        def length(self, point):
            return np.sqrt(np.sum((self.coords - point.coords) ** 2))
        
        def __eq__(self, other):
            return np.allclose(self.coords, other.coords, atol = 1e-6)
        
        def __hash__(self):
            return hash(tuple(np.round(self.coords, decimals = 6)))

    class Circ:
        def __init__(self, r, center, ps):
            self.r = r
            self.c = center
            self.p = ps

        def __lt__(self, p):
            return self.r < p.r

    def sphere(points1):

        pointsA = np.array([point.get_coords() for point in points1])
        
        n = pointsA.shape[0]

        A = np.hstack((2 * pointsA, np.ones((n, 1))))
        b = np.sum(pointsA ** 2, axis = 1)

        x = np.linalg.lstsq(A, b, rcond = None)[0]

        center = x[:-1]
        r = x[-1] + np.sum(center ** 2)

        return center, np.sqrt(r)

    def KM(S, k, initial):
        
        S = np.array(S)

        kmeans = KMeans(n_clusters=k, init=initial, n_init = 1, random_state = 42)
    
        kmeans.fit(S)

        clusters = {i: S[kmeans.labels_ == i].tolist() for i in range(k)}

        return clusters

    delaunay = Delaunay(points)

    vertex = []

    for simplex in delaunay.simplices:
        verx = []
        for i in simplex:
            verx.append(point(points[i]))

        c, r = sphere(verx)
        vertex.append(Circ(r, c, verx))

    vertex.sort(reverse = True)

    ccenter = []
    Test = []
    Temp = []

    i = 0

    while True:

        for j in range(len(vertex[i].p)):
            f = True
            for l in range(j + 1, len(vertex[i].p)):
                if vertex[i].p[j].length(vertex[i].p[l]) < vertex[i].r:
                    f = False
            if f:
                Test.append(vertex[i].p[j])

        if len(ccenter) == 0:
            
            ccenter.extend(Test)
            
            if len(ccenter) == k:
                return KM(points, k, np.array([p.get_coords() for p in ccenter]))
            else:
                i += 1
                Test.clear()
                continue

        for j in range(len(ccenter)):
            for l in range(len(Test)):
                if ccenter[j].length(Test[l]) < vertex[i].r:
                    Temp.append(Test[l])

        ccenter.extend([point for point in Test if point not in Temp and point not in ccenter])

        if len(ccenter) == k:
            return KM(points, k, np.array([p.get_coords() for p in ccenter]))

        i += 1
        Test.clear()
        Temp.clear()
