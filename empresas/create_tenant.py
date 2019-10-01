from empresas.models import Empresa
tenant = Empresa(domain_url = 'configuracion.local',
                schema_name = 'public',
                nombre = 'Kirios Net',
                )
tenant.save()  
tenant = Empresa(domain_url = 'titu.configuracion.local',
                schema_name = 'titu',
                nombre = 'Titu Cocktail Xpress',
                )
tenant.save()  
tenant = Empresa(domain_url = 'lasalva.configuracion.local',
                schema_name = 'lasalva',
                nombre = 'La Salva burguer',
                )
tenant.save()