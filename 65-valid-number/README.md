<h2><a href="https://leetcode.com/problems/valid-number/">65. Valid Number</a></h2><h3>Hard</h3><hr><div style="user-select: auto;"><p style="user-select: auto;">A <strong style="user-select: auto;">valid number</strong> can be split up into these components (in order):</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">A <strong style="user-select: auto;">decimal number</strong> or an <strong style="user-select: auto;">integer</strong>.</li>
	<li style="user-select: auto;">(Optional) An <code style="user-select: auto;">'e'</code> or <code style="user-select: auto;">'E'</code>, followed by an <strong style="user-select: auto;">integer</strong>.</li>
</ol>

<p style="user-select: auto;">A <strong style="user-select: auto;">decimal number</strong> can be split up into these components (in order):</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">(Optional) A sign character (either <code style="user-select: auto;">'+'</code> or <code style="user-select: auto;">'-'</code>).</li>
	<li style="user-select: auto;">One of the following formats:
	<ol style="user-select: auto;">
		<li style="user-select: auto;">One or more digits, followed by a dot <code style="user-select: auto;">'.'</code>.</li>
		<li style="user-select: auto;">One or more digits, followed by a dot <code style="user-select: auto;">'.'</code>, followed by one or more digits.</li>
		<li style="user-select: auto;">A dot <code style="user-select: auto;">'.'</code>, followed by one or more digits.</li>
	</ol>
	</li>
</ol>

<p style="user-select: auto;">An <strong style="user-select: auto;">integer</strong> can be split up into these components (in order):</p>

<ol style="user-select: auto;">
	<li style="user-select: auto;">(Optional) A sign character (either <code style="user-select: auto;">'+'</code> or <code style="user-select: auto;">'-'</code>).</li>
	<li style="user-select: auto;">One or more digits.</li>
</ol>

<p style="user-select: auto;">For example, all the following are valid numbers: <code style="user-select: auto;">["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]</code>, while the following are not valid numbers: <code style="user-select: auto;">["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]</code>.</p>

<p style="user-select: auto;">Given a string <code style="user-select: auto;">s</code>, return <code style="user-select: auto;">true</code><em style="user-select: auto;"> if </em><code style="user-select: auto;">s</code><em style="user-select: auto;"> is a <strong style="user-select: auto;">valid number</strong></em>.</p>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Example 1:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "0"
<strong style="user-select: auto;">Output:</strong> true
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 2:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "e"
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;"><strong style="user-select: auto;">Example 3:</strong></p>

<pre style="user-select: auto;"><strong style="user-select: auto;">Input:</strong> s = "."
<strong style="user-select: auto;">Output:</strong> false
</pre>

<p style="user-select: auto;">&nbsp;</p>
<p style="user-select: auto;"><strong style="user-select: auto;">Constraints:</strong></p>

<ul style="user-select: auto;">
	<li style="user-select: auto;"><code style="user-select: auto;">1 &lt;= s.length &lt;= 20</code></li>
	<li style="user-select: auto;"><code style="user-select: auto;">s</code> consists of only English letters (both uppercase and lowercase), digits (<code style="user-select: auto;">0-9</code>), plus <code style="user-select: auto;">'+'</code>, minus <code style="user-select: auto;">'-'</code>, or dot <code style="user-select: auto;">'.'</code>.</li>
</ul>
</div>