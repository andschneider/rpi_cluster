# Networking

## ip tables 

For the nodes to be able to reach the internet, a NAT needs to be setup on the master node. This will allow forwarding from the `wlan0` to `eht0`.

```bash
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -o eth0 -m state \
  --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```

## static ip

Set a static IP address for the cluster's internal network by modifying the file at `/etc/dhcpcd.conf`. Normally this would be added to `/etc/network/interfaces/eth0`, however, Raspbian Stretch uses `dhcpcd` to configure network interfaces.

  *Apparently the file at `/etc/network/interfaces.d/eth0` is still needed*

  ```
  allow-hotplug eth0
  iface eth0 inet static
    address 10.0.0.1
    netmask 255.255.255.0
    broadcast 10.0.0.255
    gateway 10.0.0.1
  ```

## flannel

Once the cluster is set up, Pod-to-Pod networking needs to be configured. Flannel is a tool that does this easily. Using the flannel configuration file, use `kubectl` to apply it:

`kubectl apply -f kube-flannel.yaml`
