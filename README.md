%% Strategy A1 — Bastion + NAT per AZ (HA)
flowchart TB
  Internet((Internet)) --> IGW[IGW]

  subgraph VPC[ VPC 10.10.0.0/16 ]
    direction TB

    subgraph AZa[AZ-a]
      subgraph PubA[Public Subnet a]
        ALBa[ALB (a)]
        NATa[NAT GW (a)]
        Bastion[Bastion EC2\n(22 from Office IP)]
      end
      subgraph PrivA[Private Subnet a]
        WebA[WEB/WAS EC2]
      end
      subgraph DBA[DB Subnet a]
        RDSa[(RDS)]
      end
    end

    subgraph AZc[AZ-c]
      subgraph PubC[Public Subnet c]
        ALBc[ALB (c)]
        NATc[NAT GW (c)]
      end
      subgraph PrivC[Private Subnet c]
        WebC[WEB/WAS EC2]
      end
      subgraph DBC[DB Subnet c]
        RDSc[(RDS)]
      end
    end

    S3EP[S3 Gateway Endpoint]
    SSMEP[SSM & SSMMessages\nInterface Endpoints]
  end

  IGW --> ALBa
  IGW --> ALBc
  ALBa --- ALBc

  ALBa --> WebA
  ALBc --> WebC
  WebA --> RDSa
  WebC --> RDSc

  %% egress and private connectivity
  WebA --> NATa
  WebC --> NATc
  WebA --> S3EP
  WebC --> S3EP
  WebA --> SSMEP
  WebC --> SSMEP
