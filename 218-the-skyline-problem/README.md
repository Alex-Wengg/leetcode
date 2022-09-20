<h2><a href="https://leetcode.com/problems/the-skyline-problem/">218. The Skyline Problem</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A city's <strong style="user-select: auto;">skyline</strong> is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return <em style="user-select: auto;">the <strong style="user-select: auto;">skyline</strong> formed by these buildings collectively</em>.</p>

<p style="user-select: auto;">The geometric information of each building is given in the array <code style="user-select: auto;">buildings</code> where <code style="user-select: auto;">buildings[i] = [left<sub style="user-select: auto;">i</sub>, right<sub style="user-select: auto;">i</sub>, height<sub style="user-select: auto;">i</sub>]</code>:</p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">left<sub style="user-select: auto;">i</sub></code> is the x coordinate of the left edge of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> building.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">right<sub style="user-select: auto;">i</sub></code> is the x coordinate of the right edge of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> building.</li>
	<li style="user-select: auto;"><code style="user-select: auto;">height<sub style="user-select: auto;">i</sub></code> is the height of the <code style="user-select: auto;">i<sup style="user-select: auto;">th</sup></code> building.</li>
</ul>

<p style="user-select: auto;">You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height <code style="user-select: auto;">0</code>.</p>

<p style="user-select: auto;">The <strong style="user-select: auto;">skyline</strong> should be represented as a list of "key points" <strong style="user-select: auto;">sorted by their x-coordinate</strong> in the form <code style="user-select: auto;">[[x<sub style="user-select: auto;">1</sub>,y<sub style="user-select: auto;">1</sub>],[x<sub style="user-select: auto;">2</sub>,y<sub style="user-select: auto;">2</sub>],...]</code>. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate <code style="user-select: auto;">0</code> and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.</p>

<p style="user-select: auto;"><b style="user-select: auto;">Note:</b> There must be no consecutive horizontal lines of equal height in the output skyline. For instance, <code style="user-select: auto;">[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]</code> is not acceptable; the three lines of height 5 should be merged into one in the final output as such: <code style="user-select: auto;">[...,[2 3],[4 5],[12 7],...]</code></p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="width: 800px; height: 331px; user-select: auto;">
<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
<strong style="user-select: auto;">Output:</strong> [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
<strong style="user-select: auto;">Explanation:</strong>
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> buildings = [[0,2,3],[2,5,3]]
<strong style="user-select: auto;">Output:</strong> [[0,3],[5,0]]
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= buildings.length &lt;= 10<sup style="user-select: auto;">4</sup></code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">0 &lt;= left<sub style="user-select: auto;">i</sub> &lt; right<sub style="user-select: auto;">i</sub> &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= height<sub style="user-select: auto;">i</sub> &lt;= 2<sup style="user-select: auto;">31</sup> - 1</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">buildings</code> is sorted by <code style="user-select: auto;">left<sub style="user-select: auto;">i</sub></code> in&nbsp;non-decreasing order.</li>
</ul>
</div>