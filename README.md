## Configure git

``` bash

git config --global user.name xolar1989
git config --global user.email xolar1989@o2.pl
git init 
git remote add origin https://github.com/xolar1989/lawyer-llm
git fetch origin



```

## Configure BastionHost for mongodb local

```bash

ssh tunnel to bastion
 ssh -i "BASTION_KEYS.pem" -L 27017:documentdb-cluster.cluster-cywgk7qvlcrn.eu-central-1.docdb.amazonaws.com:27017 ubuntu@ec2-3-69-31-158.eu-central-1.compute.amazonaws.com -N




```


