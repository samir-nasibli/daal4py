#*******************************************************************************
# Copyright 2014-2018 Intel Corporation
# All Rights Reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License"), the following terms apply:
#
# You may not use this file except in compliance with the License.  You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#*******************************************************************************

# daal4py outlier detection univariate example for shared memory systems

import daal4py as d4p
import numpy as np

# let's try to use pandas' fast csv reader
try:
    import pandas
    read_csv = lambda f, c, t=np.float64: pandas.read_csv(f, usecols=c, delimiter=',', header=None, dtype=t)
except:
    # fall back to numpy loadtxt
    read_csv = lambda f, c, t=np.float64: np.loadtxt(f, usecols=c, delimiter=',', ndmin=2)


def main():
    # Input file
    infile = "./data/batch/outlierdetection.csv"

    # Retrieve the data from the input file
    data = read_csv(infile, range(3))

    # Create an algorithm to detect outliers (univariate)
    algorithm = d4p.univariate_outlier_detection()

    # Compute outliers and get the computed results
    res = algorithm.compute(data, None, None, None)

    # result provides weights
    assert res.weights.shape == (data.shape[0], 3)

    return (data, res)


if __name__ == "__main__":
    (data, res) = main()

    print("\nInput data\n", data)
    print("\nOutlier detection result (univariate) weights:\n", res.weights)
    print('All looks good!')
