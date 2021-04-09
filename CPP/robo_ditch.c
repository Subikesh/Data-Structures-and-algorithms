int robo_ditch(int nf, int nb, int fd, int bd, int time) {
    int unit = nf-nb, steps = 0, i;
    bd = -bd;
    if(nf >= fd) {
        steps += time*fd;
        printf("F %d", steps);
    }
    else if(nb-nf >= -bd) {
        steps += time*((2*nf)+bd);
        printf("B %d", steps);
    }
    else if(unit == 0) {
        printf("NO");
    }
    else if(unit > 0) {
        for(i=0; i<fd; i += unit) {
            steps += time*(nf+nb);
        }
        printf("F %d", steps);
    }
    else {
        for(i=0; i>bd; i-=unit) {
            steps += time*(nf+nb);
        }
        printf("B %d", steps);
    }
}

