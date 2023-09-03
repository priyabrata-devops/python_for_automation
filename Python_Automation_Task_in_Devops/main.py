import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

# get default vpc information
for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_sets:
        print(assoc_set["CidrBlockState"])

# create a vpc
create_new_vpc = ec2_client.create_vpc(
    CidrBlock='192.168.0.0/16',
)

create_new_subnet = create_new_vpc.create_subnet(
    CidrBlock='192.168.1.0/24',
)

create_new_subnet = create_new_vpc.create_subnet(
    CidrBlock='192.168.2.0/24',
)
