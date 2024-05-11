== System Health ==

<pre>
SFC /scannow

DISM /online /cleanup-image /restorehealth
</pre>

== Issues ==

=== Window not blanking ===

assuming you have screen blanking enabled, check whats holding it open

<pre>
powercfg -requests
</pre>
