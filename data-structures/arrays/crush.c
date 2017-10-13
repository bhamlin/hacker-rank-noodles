#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main() {
    int n, m, a, b, c, i, t = 0;
    long max = 0;
    long* data;
    
    scanf("%i %i", &n, &m);
    
    data = (long*)calloc( n + 1, sizeof(long) );
    
    for(i = 0; i < m; i++) {
        scanf("%i %i %i", &a, &b, &c);
        
        data[a - 1] += c;
        data[b] -= c;
    }
    
    for(t = data[0], i = 1; i < n; i++) {
        t += data[i];
        if(max < t) {
            max = t;
        }
    }
    
    printf("%ld\n", max);
    
    free(data);
    
    return 0;
}
