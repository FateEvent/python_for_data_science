#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <stdio.h>

int	main(int ac, char *av[])
{
	int fd;
	
	if (ac == 2)
	{
		fd = open(av[1], O_WRONLY | O_APPEND | O_CREAT, 0664);
		if (fd == -1)
			return(1);
		write(fd, "\r", 1);
		close(fd);
	}
}
