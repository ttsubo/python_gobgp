What's python_gobgp
==========
GoBGPのneighbor/prefix追加をpythonスクリプトから実施できるツールです.

インストール
==========
etcdをインストールする.

	$ curl -L  https://github.com/coreos/etcd/releases/download/v2.3.4/etcd-v2.3.4-linux-amd64.tar.gz -o etcd-v2.3.4-linux-amd64.tar.gz
	$ sudo tar -C /usr/local/sbin -xzvf etcd-v2.3.4-linux-amd64.tar.gz
	$ cd /usr/local/sbin/etcd-v2.3.4-linux-amd64	
	$ ./etcd -version
	etcd Version: 2.3.4
	Git SHA: df60227
	Go Version: go1.6.2
	Go OS/Arch: linux/amd64

	$ vi .profile

	--------------------
	... snip
	$ export PATH=$PATH:$GOPATH/bin:/usr/local/go/bin:/usr/local/sbin/etcd-v2.3.4-linux-amd64
	$ source .profile


etcdのクラスタ構成を設定する.

	$ cd /etc/init
	$ sudo vi etcd.conf

	--------------------
	description "etcd service registry"

	start on runlevel [2345]
	stop on runlevel [!2345]

	respawn


	script
	  /usr/local/sbin/etcd-v2.3.4-linux-amd64/etcd \
	    -heartbeat-interval=500 \
	    -election-timeout=2500 \
	    -snapshot-count=5000 \
	    -initial-cluster-token etcd-cluster-1 \
	    -initial-cluster GoBGP-1=http://192.168.183.236:2380,GoBGP-2=http://192.168.183.235:2380,GoBGP-3=http://192.168.183.131:2380 \
	    -initial-cluster-state new \
	    -initial-advertise-peer-urls http://192.168.183.236:2380 \
	    -advertise-client-urls http://192.168.183.236:2379 \
	    -listen-client-urls http://192.168.183.236:2379 \
	    -listen-peer-urls http://192.168.183.236:2380 \
	    -data-dir /var/cache/etcd/state \
	    -name GoBGP-1
	end script


etcdのクラスタ構成を設定する.

	$ sudo service etcd start
	$ sudo service etcd status
	etcd start/running, process 18093


Githubから、リポジトリを取得して、インストールします.

	$ sudo apt-get update
	$ sudo apt-get install python-pip
	$ sudo apt-get install python-dev
	$ git clone https://github.com/ttsubo/python_gobgp.git
	$ cd python_gobgp
	$ sudo pip install -r pip-requires.txt
