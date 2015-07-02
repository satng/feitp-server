### English ###
**1.Maybe this is the most powerful ftp server library in this world.**<br>
2.Developed on Python pyftp lib, thanks for the suggestion from Author in 3 months communication <br>
3.With Multiprocess library, feitp-server uses multi-cpu resources to promote performance. <br>
4.10X times than Vsftp, 5X times than pyftplib (Depend on your hardware capability) <br>
5.Good stability in 5 millions clients in Shanghai TV box ftp product environment. <br>
6.Easy expend and left API to developer like Login,upload,logout etc. <br>
<h3>Deutsch</h3>
<b>1.Das ist vielleicht die stärkste ftp-Server-Lib auf dieser Welt.</b><br>
2.Entwicklung auf Python pyftp lib. Danke für den Vorschlag von Autor während der 3 monatlichen 3.Kommunikation.<br>
4.Mit Hilfe von Multi-Prozess-Lib verwendet feitp-Server Multi-CPU-Ressourcen, um die Leistungen zu fördern. <br>
5.10 Mals schneller als Vsftp, 5 Mals schneller als pyftplib (abhängig von Ihrer Hardware-Fähigkeit) <br>
6.Gute Stabilität für 5 Millionen Kunden in Shanghai TV-Box ftp Produktumgebung. <br>
7.Leicht zur Weiterentwicklung. Es gibt API, damit Entwickler anmelden, hochladen, abmelden, usw. können.<br>

<h3>中文</h3>
<b>1.这可能是你见过或者着没见过的最强的FTP服务器兼lib代码。</b><br>
2.建立在pyftplib基础上，谢谢意大利的Python语言贡献者Giampaolo Rodola's 的建议，3个月技术支持和沟通。<br>
3.实用了多进程的lib，充分利用了多块CPU的资源能力，大大提升了性能。<br>
4.比10倍以上的vsftp的能力，5倍以上pyftplib的能力。<br>
5.非常好的稳定性，在500万上海机顶盒用户生产环境下。<br>
6.预留出了简单的API接口给开发者，实现自己的login/upload/logout逻辑<br>

+<b>Notice,it's just for linux System only.</b>=<br>
<br>
<h2>1.Python  2.6<= verison <= 2.7</h2>
because this server need multiprocess supported and pyfpdlib supported<br>

More in detail<br>
<a href='http://docs.python.org/library/multiprocessing.html'>http://docs.python.org/library/multiprocessing.html</a>     >2.6<br>
<a href='http://code.google.com/p/pyftpdlib/'>http://code.google.com/p/pyftpdlib/</a>                      2.4~2.7<br>


<h2>2.Install</h2>
<pre><code>$unzip pyftpdlib-0.6.0-By-Fei<br>
$cd pyftpdlib-0.6.0-By-Fei<br>
$python setup.py install<br>
$cd ..<br>
$vim FEITP-SERVER.py 　modify your user &amp; pwd &amp; server address &amp; port &amp; 目录 &amp; 权限<br>
$vim 修改 线程数量，建议CPU数量的两倍 NUMBER_OF_PROCESSES = multiprocessing.cpu_count()<br>
$python FEITP-SERVER.py　　running your ftp server now<br>
</code></pre>


<img src='http://farm7.static.flickr.com/6056/6333983228_a8f630433a.jpg' alt='2.7.2' width='500' height='217'>

<h2>3.Run</h2>
You need config your FTP ,PORT,USER,PWD,DIR in FEITP-SERVER<br>
Best high-Preformance use double Number of CPU for process<br>


$python FEITP-SERVER.py<br>
<br>
<h2>4.DIY your logic</h2>
If you overwrite YourHandler Class, there are a lot of your logic you can do <br>
class YourHandler(ftpserver.FTPHandler)<br>

<h2>5.Hope could you like it</h2>
Link: wu.qunfei@gmail.com<br>


<h2>6.Thinking in FTP degsin</h2>

The server was designed for a lot of clients sent file to server at same time.<br>
The code job is 3 things:<br>

First lib is pyftpdlib which is a high-level portable interface to easily write asynchronous FTP servers.<br>
Secondly, multiprocessing lib is good method let you to use multi-CPU in your machine replacing the 1 CPU running all threading.<br>
Thirdly, I rewrite the pyftpdlib sourcecode.<br>

Some params need to config<br>
1.In Linux<br>
$ulimit -n max_open_file_number<br>
$ulimit -s min_buffer_in_one_thread<br>

2.In Process<br>
I suggest that you can use double of your CPU number for yout ftp processes.<br>
Process(N) = CPU(N) <b>2</b><br>

4.In FTP<br>

tcp_no_delay = True<br>
max_connection = max_your_can<br>
use_simply_auth when you login<br>
the default of income_buffer which you can change with your logic<br>

1900 TPS for 50 Client together,No failed,Response at 0.005~0.0035 ms.<br>
Every client send server a 1K~4K file together.<br>


Test Much better than VSFTP server,VSFTP(JUST 268TPS)<br>

<a href='http://www.flickr.com/photos/wuqunfei/6331353252/' title='Flickr 上 wuqunfly 的 1900并发'><img src='http://farm7.static.flickr.com/6108/6331353252_8d435a1e0c.jpg' alt='1900并发' width='500' height='291'>


