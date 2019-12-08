# Ansible configurations

## Initial set up

Installs:

- Docker 19.03
- Kubernetes 1.16.3

Run playbook:

```bash
ansible-playbook -i hosts init_config.yml -v
```

## Master node set up

*WIP*

Sets up networking on the master node.

Run playbook:

```bash
ansible-playbook -i hosts master_config.yml -v
```
